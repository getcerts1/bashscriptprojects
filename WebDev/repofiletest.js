const GenerateRandomNum = ''

for (let i=0; i < 20; i++) {
  i+=GenerateRandomNum
}

console.log(GenerateRandomNum)

//this is a message

const array1 = [
  {
    name: 'product1',
    image: '',
    rating: {
      stars: 4.5,
      count: 45
    },
    priceCents: 1099
  },
  {
    name: 'product2',
    image: ``,
    rating: {
      stars: 4.5,
      count: 21
    },
    priceCents: 2045
  }
]

let renderHTML = ''

array1.forEach((item) => {
  html = `<div class="container">
  <div class="image-container"><img src="product-1-image.jpeg" class="product-image"></div>
  <div class="product-info">
    <div class="product-name">${item.name}</div>
    <div class="product-rating">${item.rating}</div>
    <div class="product-price">${item.priceCents}</div>
  </div>
 </div>`

 renderHTML+=html
})

document.querySelector('.doc-grid')
  .innerHTML = renderHTML
