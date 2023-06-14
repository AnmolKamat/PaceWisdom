//write an function to check if a object has properties

function hasProperties(obj) {
    for (var key in obj) {
        if (obj.hasOwnProperty(key)) {
            return true;
        }
    }
    return false;
}