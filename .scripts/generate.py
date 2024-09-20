import os
import re
from anthropic import Anthropic
from problems import leetcode_problems
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


# Anthropic API key (replace with your actual key)
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
anthropic = Anthropic(api_key=ANTHROPIC_API_KEY)
anthropic_usage = 0


def snake_case(s):
    return re.sub('[ /-]+', '_', s.lower())


def create_directory(path):
    os.makedirs(path, exist_ok=True)

def get_problem_description(url, browser, timeout=30000):  # timeout in milliseconds
    page = browser.new_page()
    try:
        page.goto(url)

        # Wait for the content to load, with a timeout
        try:
            page.wait_for_selector('[data-track-load="description_content"]', timeout=timeout)
        except PlaywrightTimeoutError:
            raise TimeoutError(f"Timeout waiting for description content on {url}")

        # Get the description content
        description_element = page.query_selector('[data-track-load="description_content"]')
        if description_element:
            description = description_element.inner_text()
            return description.strip()
        else:
            raise ValueError(f"No description element found on {url}")
    finally:
        page.close()


def generate_unittest(problem_description, anthropic):
    message = anthropic.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": f"""
Create a Python unittest for the following LeetCode problem:

{problem_description}

Instructions:
- Provide only the raw Python code for the unittest, without any additional explanation or formatting.
- Do not use markdown code blocks or any other formatting.
- Start your response with 'import unittest' and end it with 'if __name__ == '__main__':'.
- Do not include any other text before or after the code.
- Do not include the solution, only the unittest"""
            }
        ]
    )
    print('Used tokens', message.usage.input_tokens + message.usage.output_tokens)
    global anthropic_usage
    anthropic_usage += message.usage.input_tokens + message.usage.output_tokens
    return message.content[0].text

def generate_readme(problem_description, anthropic):
    message = anthropic.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": f"""Traduce la siguiente descripción de un problema de LeetCode al español:

{problem_description}

Instrucciones:
1. Realiza una traducción fluida y natural, evitando una traducción literal.
2. Adapta el texto para que suene natural en español, manteniendo el significado original.
3. Utiliza terminología técnica apropiada en español cuando sea necesario.
4. Formatea el resultado como un archivo markdown, incluyendo:
   - Un título principal con el nombre del problema
   - Secciones claramente definidas (Descripción, Ejemplos, Restricciones, etc.)
5. Asegúrate de que la explicación sea clara y fácil de entender para hablantes nativos de español.

Proporciona solo el contenido markdown resultante, sin explicaciones adicionales."""
            }
        ]
    )
    print('Used tokens', message.usage.input_tokens + message.usage.output_tokens)
    global anthropic_usage
    anthropic_usage += message.usage.input_tokens + message.usage.output_tokens
    return message.content[0].text

def main():
    base_path = "./"
    error_file = os.path.join(base_path, 'errors.txt')

    with open(error_file, 'w') as error_log:
        for category, problems in leetcode_problems.items():
            category_path = os.path.join(base_path, '..', snake_case(category))
            create_directory(category_path)

            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False)
                for problem in problems:
                    problem_name = problem['name']
                    problem_url = problem['url']

                    # Extract problem name for directory
                    problem_dir_name = problem_url.split('/')[-2]
                    problem_path = os.path.join(category_path, snake_case(problem_dir_name))
                    if os.path.exists(problem_path):
                        print(f"Skipping existing problem directory: {problem_path}")
                        continue

                    try:
                        # Get the problem description
                        problem_description = get_problem_description(problem_url, browser)

                        print(f'Generating unnitest for {problem_name}')
                        unittest_content = generate_unittest(problem_description, anthropic)

                        print(f'Generating readme for {problem_name}')
                        readme_content = generate_readme(problem_description, anthropic)

                        create_directory(problem_path)

                        # Generate and save unittest
                        with open(os.path.join(problem_path, 'test_solution.py'), 'w') as f:
                           f.write(unittest_content)

                        # Generate and save README.md
                        with open(os.path.join(problem_path, 'README.md'), 'w') as f:
                           f.write(readme_content)

                        print(f"Processed: {problem_name}")

                    except Exception as e:
                        error_message = f"{problem_name}, Error: {str(e)}\n"
                        error_log.write(error_message)
                        print(f"Error processing {problem_name}: {str(e)}")

                browser.close()

    print('Used tokens so far: ', anthropic_usage)

if __name__ == "__main__":
    main()
