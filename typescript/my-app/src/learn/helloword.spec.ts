//#region helloworld
// --------------------------------------------------
// helloworld
// --------------------------------------------------
describe('hello', () => {
    it('test hello world', () => {
        console.log('hello world!');
    });
});
//#endregion helloworld
//#region getFactorial
// --------------------------------------------------
// getFactorial
// --------------------------------------------------
function getFactorial (number) {
    if (number < 0) {
        throw new Error('There is no factorial for negative numbers');
    } else if ( number === 1 || number === 0) {
        return 1;
    } else {
        return number * getFactorial(number - 1);
    }
}
function signum(number) {
    if (number > 0) {
        return 1;
    } else if (number === 0) {
        return 0;
    } else {
        return -1;
    }
}
function average (number1, number2) {
    return (number1 + number2) / 2;
}

describe('when using getFactorial', () => {
    it('should be able to find factorial for positive number', () => {
        expect(getFactorial(3)).toEqual(6);
    });
    it('should be able to find factorial for 0', () => {
        expect(getFactorial(0)).toEqual(1);
    });
    it('should be able to throw an exception when number is negative', () => {
        expect(function() {
            getFactorial(-10);
        }).toThrow(new Error('There is no factorial for negative numbers'));
    });
});
//#endregion getFactorial
