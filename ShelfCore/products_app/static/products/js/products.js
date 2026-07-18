// to open edit or view modal window
const InfoBtns = document.querySelectorAll('.info-btn');
const EditBtns = document.querySelectorAll('.edit-btn');
// general modal window
const modal = document.querySelector('.modal');
// types of modals window
const modalEdit = document.querySelector('.modal-edit');
const modalView = document.querySelector('.modal-view')
// close button for both
const CloseBtns = document.querySelectorAll('#close-modal');
// span tags for view modal
const modalName = document.querySelector('#modal-name');
const modalUnit = document.querySelector('#modal-unit');
const modalBarcode = document.querySelector('#modal-barcode');
const modalCategory = document.querySelector('#modal-category');
const modalIsActive = document.querySelector('#modal-is-active');
const modalIsAgeRestricted = document.querySelector('#is-age-restricted');
// inputs tags for edit modal
// const modalNameEdit = document.querySelector('#modal-name-edit')
const modalEditName = document.querySelector('#edit-name');
const modalEditBarcode = document.querySelector('#edit-barcode');
const modalEditCategory = document.querySelector('#edit-category');
const modalEditUnit = document.querySelector('#edit-unit');
const modalEditAgeRestricted = document.querySelector('#edit-age-restricted');
const modalEditActive = document.querySelector('#edit-active');

function openViewModal(){
    modal.classList.add('active');

    modalView.classList.add('active');
    modalEdit.classList.remove('active');
};

function openEditModal(){
    modal.classList.add('active');

    modalView.classList.remove('active');
    modalEdit.classList.add('active');
};

function closeModal(){
    modal.classList.remove('active');

    modalView.classList.remove('active');
    modalEdit.classList.remove('active');
};

CloseBtns.forEach(button => {
    button.addEventListener(
        'click',
        closeModal,
    )
});

InfoBtns.forEach(button => {
    button.addEventListener(
            'click',
            () => {
                const id = button.dataset.id;
                console.log('View', id);
                fetch(`/products/${id}/info/`)
                    .then(response => response.json())
                    .then(data => {
                        modalName.textContent = data.name;
                        modalBarcode.textContent = data.barcode;
                        modalUnit.textContent = data.unit;
                        modalCategory.textContent = data.category;
                        modalIsActive.textContent =
                            data.is_active ? "✅" : "❌";
                        modalIsAgeRestricted.textContent =
                            data.age_restricted ? "🔞" : "✅";
                        openViewModal();
                    });
            }
        );
});

EditBtns.forEach(button=>{
    button.addEventListener(
        'click',
        () =>{
            const id = button.dataset.id;
            fetch(`/products/${id}/info/`)
                .then(response => response.json())
                .then(data =>{
                    modalEditName.value = data.name;
                    modalEditBarcode.value = data.barcode;
                    modalEditCategory.value = data.category_id;
                    modalEditUnit.value = data.unit;
                    modalEditAgeRestricted.checked = data.age_restricted;
                    modalEditActive.checked = data.is_active;
                    openEditModal();
                });
        }
    );
});