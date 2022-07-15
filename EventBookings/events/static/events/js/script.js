// Forms Close Buttons
const formCloseBtns = document.querySelectorAll(".close");

formCloseBtns.forEach((btn) =>
  btn.addEventListener("click", (e) => {
    e.target.parentElement.classList.add("hide");
  })
);

// Edit Page: Edit Forms
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

// Profile Page: Edit Profile Details
const profileSelectBtns = document.querySelectorAll(".profile-menu button");
const profileEditForm = document.getElementById("profile-edit");

profileSelectBtns.forEach((btn) =>
  btn.addEventListener("click", (e) => {
    profileEditForm.classList.remove("hide");
  })
);
