function arrayPlusArray(arr1, arr2) {
    return Array().concat(...arr1, ...arr2).reduce((acc, value) => acc + value, 0)
  }
c = arrayPlusArray([1,2,3], [4,5,6])
console.log(c)

  