package ransom_note

func canConstruct(ransomNote string, magazine string) bool {
	count := make(map[byte]int)
	for _, r := range magazine {
		current, ok := count[byte(r)]
		if !ok {
			count[byte(r)] = 1
		} else {
			count[byte(r)] = current + 1
		}
	}

	for _, r := range ransomNote {
		current, ok := count[byte(r)]
		if !ok {
			return false
		} else {
			count[byte(r)] = current - 1
		}
	}

	for _, count := range count {
		if count < 0 {
			return false
		}
	}

	return true
}
