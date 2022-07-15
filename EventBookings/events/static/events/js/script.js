// Edit Page Edit Forms
const editSelectBtns = document.querySelectorAll(".edit-menu button");
const editForms = document.querySelectorAll(".edit-form");

editSelectBtns.forEach((btn) =>
  btn.addEventListener("click", (e) => {
    editForms.forEach((form) => {
      form.classList.add("hide");
      if (form.id === e.target.value.toLowerCase()) {
        console.log("uwu");
        form.classList.remove("hide");
      }
    });
  })
);
