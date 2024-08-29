// tier 7

const vowelCount = (str) => {
    const vowelsList = ['a', 'e', 'i', 'o', 'u'];
    const words = str.split('')
    let count = 0
    words.forEach(element => {
        return vowelsList.includes(element) ? count++ : 0 
    });
    return count
}

console.log(vowelCount('abracadabra'))

// function getCount(str) { return (str.match(/[aeiou]/ig)||[]).length;} // Este es mas resumido esta bueno.
//function getCount(str) { return str.split('').filter(c => "aeiouAEIOU".includes(c)).length; } // Otro que ocupa filter
// function getCount(str) { return str.replace(/[^aeiou]/gi, '').length; } // replace