const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {
  return val.toString().toLowerCase().trim()
    .replace(/&/g, '-and-') // replace & with '-and-'
    .replace(/[\s\W-]+/g, '-'); // replace whitespace and non-word characters with '-'
};

titleInput.addEventListener('keyup', (e) => {
  slugInput.value = slugify(titleInput.value); // Use property directly for better performance
});
