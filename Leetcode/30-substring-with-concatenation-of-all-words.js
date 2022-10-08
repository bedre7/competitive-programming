/**
 * @param {string} s
 * @param {string[]} words
 * @return {number[]}
 */
 const findSubstring = function(s, words)
 {
     let strLen = words.length * words[0].length;
     let str = '';
     let indices = [];
     let wordsStr = words.join('');
     for(let i = 0; i <= s.length - strLen; i++)
     {
         str = s.slice(i, strLen + i);
 
         let token; 
         for(let j = 0; j < str.length; j += words[0].length)
         {
             token = str.slice(j, words[0].length + j);
             if(wordsStr.includes(token))
             {
                 if(wordsStr.indexOf(token) % words[0].length === 0)
                     wordsStr = wordsStr.replace(token, '');
                 else if(wordsStr.lastIndexOf(token) % words[0].length === 0)
                 {
                     wordsStr = wordsStr.slice(0, wordsStr.lastIndexOf(token));
                 }
             }
         }
         if(wordsStr === '')
             indices.push(i);
         wordsStr = words.join('');
     }
     return indices;
 }