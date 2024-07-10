const denth = 5

function pyramids(denth, count = 1, length = denth, result = '') {
    for (let integ = 0;integ < length; integ++) {
        if (integ < count) result += integ + 1
        else result += '.'
    }
    for (let integ = length; integ > 0; integ--) {
        if (count >= integ) result += integ
        else result += '.'
    }
    result += '\n'
    if (denth > 1)
        return pyramids(denth - 1, count + 1, length, result)
    return result
}

console.log(pyramids(denth))