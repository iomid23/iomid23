const aText = [
  "hi, i'm ron", // add your text
  "a web developer", // add your text
  "based in riga, latvia", // add your text
  "i drink a lot of tea", // add your text
  "and build beautiful websites" // add your text
];
const iSpeed = 100; 
let iIndex = 0; 
let iArrLength = aText[0].length; 
const iScrollAt = 20; 
let iTextPos = 0; 
let sContents = ''; 
let iRow; 

function typewriter() {
  sContents = '';
  iRow = Math.max(0, iIndex - iScrollAt);
  const destination = document.getElementById("typedtext");

  while (iRow < iIndex) {
    sContents += aText[iRow++] + '<br />';
  }

  destination.innerHTML = sContents + aText[iIndex].substring(0, iTextPos) + "_";

  if (iTextPos++ === iArrLength) {
    iTextPos = 0;
    iIndex++;

    if (iIndex !== aText.length) {
      iArrLength = aText[iIndex].length;
      setTimeout(typewriter, 500);
    }
  } else {
    setTimeout(typewriter, iSpeed);
  }
}

typewriter();
