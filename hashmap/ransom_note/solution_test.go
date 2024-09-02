package ransom_note

import "testing"

func TestPossibleRansomNote(t *testing.T) {
	actual := canConstruct("aa", "aab")
	if !actual {
		t.Errorf("Expected %t to be true", actual)
	}
}

func TestImpossibleRansomNote(t *testing.T) {
	actual := canConstruct("aabc", "aa")
	if actual {
		t.Errorf("Expected %t to be true", actual)
	}
}
