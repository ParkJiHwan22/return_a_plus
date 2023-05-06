const form = document.querySelectorAll('#likeform')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
form.forEach( (likeform) => {
  likeform.addEventListener('submit', function (event) {
    event.preventDefault()
    const postId = event.target.dataset.postId
    console.log(likeform)
    axios({
      method: 'POST',
      url: `/${postId}/like/`,
      headers: {'X-CSRFToken':csrftoken,}
    })
    .then((response) => {
      const islikeusers = response.data.is_like_users
      const likeBtn = document.querySelector('#likeform > div > input[type=submit]')
      console.log(likeBtn)
      if (islikeusers === true) {
        likeBtn.value = "Cancel"
      } else {
        likeBtn.value = "Like"
      }
    })
  })
})
// form.addEventListener('submit', function (event) {
//   event.preventDefault()
//   const postId = event.target.dataset.postId
//   axios({
//     method: 'POST',
//     url: `/${postId}/like/`,
//     headers: {'X-CSRFToken':csrftoken,}
//   })
//   .then((response) => {
//     const islikeusers = response.data.is_like_users
//     const likeBtn = document.querySelector('#like-form > div > input[type=submit]')
//     console.log(likeBtn)
//     console.log(likeBtn)
//     if (islikeusers === true) {
//       likeBtn.value = "Cancel"
//     } else {
//       likeBtn.value = "Like"
//     }
//   })
// })
