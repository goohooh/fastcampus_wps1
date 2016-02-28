function addAttribute(element, property, value) {
	var old_prop = element.getAttribute(property);
	if (old_prop) {
		// 존재한다면 보존
		element.setAttribute(property, old_prop + ' ' +value);
	} else {
		element.setAttribute(property, value);
	}

}

function selector(element, parent) {
    // 유효성 감사 (Validation)


    //삼항식, 더 간단하다 => 조건 ? 참(실행) : 거짓(실행)
    //return els.length === 1 ? els[0] : els;
    //return !els ? null : els.length > 1 ? else : els[0];

    var els = (parent || document).querySelectorAll(element);
    //if (parent) {
    //    els = parent.querySelectorAll(element);
    //} else {
    //    els = document.querySelectorAll(element);
    //}
    return !els ? null : els.length > 1 ? els : els[0];

}

function isType(data, data_type) {
    //내가 만든 코드
    //if (data_type === data.constructor) {
    //    return true
    //} else {
    //    return false
    //}

    //선생님 코드
    //if (data === undefined || data === null) {
    //    return data;
    //} else {
    //    return data.constructor === data_type;
    //}

    //보완방식(call 사용)
    if (typeof data_type !== 'string') {
        throw new Error('두번째 인자는 문자열이어야 합니다.')
    }
    return Object.prototype.toString.call(data).slice(8, -1).toLowerCase() === data_type.toLowerCase();
}