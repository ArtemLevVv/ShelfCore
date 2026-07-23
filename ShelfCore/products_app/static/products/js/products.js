// to open edit or view modal window
const InfoBtns = document.querySelectorAll('.info-btn');
const EditBtns = document.querySelectorAll('.edit-btn');
// general modal window
const modal = document.querySelector('.modal');
// types of modals window
const modalEdit = document.querySelector('.modal-edit');
const modalView = document.querySelector('.modal-view')
// close button for both
const closeBtns = document.querySelectorAll('.close-modal');
// save button 
const saveBtn = document.querySelector('#save-product');
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
// saves info about pk of selected product
let selectedProductId = null;

function openViewModal(){
    modal.classList.add('active');

    modalView.classList.add('active');
    modalEdit.classList.remove('active');
};

function openEditModal(pk){
    modal.classList.add('active');

    selectedProductId = pk;
    
    modalView.classList.remove('active');
    modalEdit.classList.add('active');
};

function closeModal(){
    modal.classList.remove('active');

    selectedProductId = null;

    modalView.classList.remove('active');
    modalEdit.classList.remove('active');
};

function updateProduct(id, name, barcode){
    const productDiv = document.querySelector(
        `.product[data-id="${id}"]`
    );

    console.log(id)

    const productDivName = productDiv.querySelector(
        '.product-name'
    );

    const productDivBarcode = productDiv.querySelector(
        '.product-barcode'
    );

    productDivName.textContent = name;
    productDivBarcode.textContent = barcode;
};

closeBtns.forEach(button => {
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
                    openEditModal(id);
                })
            }
        );
    });

    
    saveBtn.addEventListener(
    'click',
    ()=>{
        if (!selectedProductId) {
            return;
        };
        const data = {
            name: modalEditName.value,
            barcode: modalEditBarcode.value,
            category: modalEditCategory.value,
            unit: modalEditUnit.value,
            age_restricted: modalEditAgeRestricted.checked,
            is_active: modalEditActive.checked,
        };
        
        const csrftoken = document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        .split('=')[1];
        fetch(`/products/${selectedProductId}/edit/`, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken,
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data=>{
            if (data.success){
                updateProduct(data.product.id, data.product.name, data.product.barcode);
            }}
        )
    }
);


