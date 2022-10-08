const lengthOfLongestSubstring = function (s) {
  let maxLength = 0;

  let str = "";
  for (let i = 0, j = 0; i < s.length; i++) {

    if (str.includes(s[i])) {
      if (str.length > maxLength) maxLength = str.length;
      str = "";
      i = j++;
    }
    str += s[i];

    if (i == s.length - 1 && str.length > maxLength)
        maxLength = str.length;
  }
  return maxLength;
};

console.log(lengthOfLongestSubstring("abcabcaa"));