function inverterString(str) {
    var a = '';
    for (var i = str.length - 1; i >= 0; i--) {
        a += str[i];
    }
    return a;
}
console.log(inverterString("cachorro"));