function Monster(name, type) {
	// if (this === window)
	if (this === window) {
		return new Monster(name, type);
	}
	this.name = name;
	this.type = type;
}

Monster.prototype.crying = function () {
	return this.name + ' 울부짖다.';
}
Monster.prototype.running = function () {
	return this.name + ' 달리다.';
}
Monster.prototype.sleeping = function () {
	return this.name + ' 잠자다.';
}


function ExtendMonster(name, type) {
	// if (this === window)
	if (this === window) {
		return new ExtendMonster(name, type);
	}
	this.name = name;
	this.type = type;
}

// 프로토 타입 확장
ExtendMonster.prototype = new Monster();