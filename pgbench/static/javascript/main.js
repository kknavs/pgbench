Array.prototype.remove = function (from, to) {
    var rest = this.slice((to || from) + 1 || this.length);
    this.length = from < 0 ? this.length + from : from;
    return this.push.apply(this, rest);
};

Array.prototype.getIndex = function (label) {
    for (var i = 0; i < this.length; i++) {
        var temp = this[i].label;
        if (temp == label) {
            return i;
        }
    }
    return -1;
};

