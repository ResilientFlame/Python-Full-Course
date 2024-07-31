// const denth = 5

// function pyramids(denth, count = 1, length = denth, result = '') {
//     for (let integ = 0;integ < length; integ++) {
//         if (integ < count) result += integ + 1
//         else result += '.'
//     }
//     for (let integ = length; integ > 0; integ--) {
//         if (count >= integ) result += integ
//         else result += '.'
//     }
//     result += '\n'
//     if (denth > 1)
//         return pyramids(denth - 1, count + 1, length, result)
//     return result
// }

// console.log(pyramids(denth))

const boxes = (n) => {
    let boxes = [ ' _ ', '|_|' ];

    for (let i = 1; i < n; i++) {
        boxes = [
            boxes[0] = ' _' + boxes[0],
            ...boxes.slice(1).map((element, idx) => '|  ' + element.slice(1)),
            ...boxes.slice(1, -1).map((element, idx) => '| ' + element),
            '|_' + boxes[boxes.length - 1]
        ]
    }
    return boxes.join('\n');
}

console.log(boxes(128))