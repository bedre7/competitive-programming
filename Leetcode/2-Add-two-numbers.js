const addTwoNumbers = function(l1, l2)
{
    let num1 = l1.val + '';
    while(l1 != null)
    {
        num1 += l1.val;
        l1 = l1.next;
    }
    const intNum1 = Number(num1.split('').reverse().join('')); 
    let num2 = l2.val;

    while(l2 != null)
    {
        num2 += l2.val;
        l2 = l2.next;
    }
    const intNum2 = Number(num2.split('').reverse().join(''));
    const sum = String(intNum1 + intNum2);

    let sumList;
    if(sum.length === 1) return ListNode(s, null);

    let head = ListNode(sum[0]);
    for(let i = 1; i < sum.length; i++)
    {
        sumList = ListNode(sum[i], head);
        head = sumList;
    }
    return sumList;
}