const form = document.querySelectorAll('#likeform')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
form.forEach( (likeform) => {
  likeform.addEventListener('submit', function (event) {
    event.preventDefault()
    const postId = event.target.dataset.postId
    axios({
      method: 'POST',
      url: `http://127.0.0.1:8000/${postId}/like/`,
      headers: {'X-CSRFToken':csrftoken,}
    })
    .then((response) => {
      const likeBtn = document.querySelector(`#like-${postId}`)
      const islikeusers = response.data.is_like_users
      if (islikeusers === true) {
        likeBtn.value = "Cancel"
      } else {
        likeBtn.value = "Like"
      }
    })
  })
})
