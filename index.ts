const file = await Bun.file("./words.txt").text();
const words = file.split("\n");

const legalCharacters = "ctxglosbieh-".split("");

const legalWords = [];
for (const w of words) {
    let isWLegal = true;
    for (const c of w.split("")) {
        if (!legalCharacters.includes(c)) {
            isWLegal = false;
            break;
        }
    }

    if (isWLegal) {
        legalWords.push(w);
    }
}

for (const w of legalWords) console.log(w);
console.log(legalWords.length);

Bun.write("./legal-words.txt", legalWords.join("\n"));
