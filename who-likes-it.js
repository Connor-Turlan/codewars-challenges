function likess(names) {
	switch (names.length) {
		case 0:
			return "no one likes this";
		case 1:
			return `${names.join("")} likes this`;
		case 2:
			return `${names.join(" and ")} like this`;
		case 3:
			return `${names[0]}, ${names.splice(1, 2).join(" and ")} like this`;
		default:
			return `${names.splice(0, 2).join(", ")} and ${
				names.length - 2
			} others like this`;
	}
}

function likes2(n) {
	l = n.length;
	return `${l > 1 ? n.slice(0, l < 3 ? 2 : 1).join(", ") + " and " : ""}${
		l > 0 ? n[l - 1] : l < 4 ? "no one" : `${l - 2} others`
	} like${l <= 1 ? "s" : ""} this`;
}

function likes(n) {
	l = n.length;
	return `${l > 2 ? n.shift() + ", " : ""}${l > 0 ? n.shift() : "no one"}${
		l > 1 ? ` and ${l > 3 ? `${l - 2} others` : n.shift()}` : ""
	} like${l < 2 ? "s" : ""} this`;
}
