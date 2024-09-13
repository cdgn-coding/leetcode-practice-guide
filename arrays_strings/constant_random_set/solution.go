package constant_random_set

import (
	"math/rand"
)

type RandomizedSet struct {
	elements map[int]int
	array    []int
}

func Constructor() RandomizedSet {
	return RandomizedSet{
		elements: make(map[int]int),
		array:    make([]int, 0),
	}
}

func (this *RandomizedSet) Insert(val int) bool {
	_, ok := this.elements[val]
	if !ok {
		_ = append(this.array, val)
		this.elements[val] = len(this.array) - 1
		return true
	}

	return false
}

func (this *RandomizedSet) Remove(val int) bool {
	_, ok := this.elements[val]
	if ok {
		delete(this.elements, val)
		return true
	}

	return false
}

func (this *RandomizedSet) GetRandom() int {
	var value int
	var index int
	var ok bool
	n := len(this.array)
	for {
		index = rand.Intn(n)
		value = this.array[index]
		_, ok = this.elements[value]
		if ok {
			return value
		}
	}
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */
