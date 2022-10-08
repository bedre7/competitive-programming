//This program checks whether an integer is palindromic or not
//e.g 121 is palindromic while 123 is not

const isPalindrome = (str) => str+'' === (str+'').split('').reverse().join('');

console.log(isPalindrome(121));