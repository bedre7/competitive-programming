'use strict'

const days = new Map([
    [1, 'Mon'],
    [2, 'Tue'],
    [3, 'Wed'],
    [4, 'Thur'],
    [5, 'Fri'],
    [6, 'Sat'],
    [7, 'Sun']
]);

const months = new Map([
    [1, 'Jan'],
    [2, 'Feb'],
    [3, 'Mar'],
    [4, 'Apr'],
    [5, 'May'],
    [6, 'Jun'],
    [7, 'Jul'],
    [8, 'Aug'],
    [9, 'Sep'],
    [10, 'Oct'],
    [11, 'Nov'],
    [12, 'Dec']
])
const getMonthPeak = function(i, year)
{
    const month = months.get(i);
    if(month === 'Feb')
    {
        if(year % 400 === 0)
            return 29;
        if(year % 4 === 0 && year % 100 !== 0) return 29;
        return 28;
    }
    return (i === 4 || i === 6 || i === 9 || i === 11) ? 30 : 31;
}
const countSundays = function(startYear)
{
    let sundays = 0, currentDate = 2;
    
    for(let year = startYear; year <= 2000; year++)
    {
        for(let currentMonth = 1; currentMonth <= 12; currentMonth++)
        {
            let monthPeak = getMonthPeak(currentMonth, year);
            for(let day = 1; day <= monthPeak; day++)
            {
                if(day === 1 && days.get(currentDate) === 'Sun') sundays++;
                currentDate++;
                if(currentDate === 8) currentDate = 1;
            }
        }
    }
    return sundays;
}

let day = 1, month = 1, year = 1901;
console.log(countSundays(year));