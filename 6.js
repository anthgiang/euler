/** [1 + ... + 100]^2 - [(1)^2 + ... + (100)^2] */

console.time(); /** Timer: start */

Array(100)
  .fill()
  .map((x, i) => i + 1)
  .reduce((prev, curr) => prev + curr) **
  2 -
  Array(100)
    .fill()
    .map((x, i) => (i + 1) ** 2)
    .reduce((prev, curr) => prev + curr);

console.timeEnd(); /** Timer: finish */
