/**
 * @param {number} x
 * @return {number}
 */
 var reverse = function(x) {
    const reversed = String(x).split('').reverse('').join('').replace('-', '');
    return Math.pow(2, 31) < reversed ? 0 : String(x).includes('-') ? -reversed : reversed;
  };