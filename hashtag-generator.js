function generateHashtag(str) {
	const tag = str
		.split(" ")
		.map((w) => w.charAt(0).toUpperCase() + w.toLowerCase().slice(1))
		.join("");
	return tag.length < 140 && tag ? "#" + tag : false;
}
