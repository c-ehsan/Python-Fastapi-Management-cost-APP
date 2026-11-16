
document.addEventListener("DOMContentLoaded", () => {

    // ============================
    // DOM Elements
    // ============================

    const createExpenseForm = document.getElementById("createExpenseForm");
    const searchInput = document.getElementById("searchInput");
    const expensesTable = document.getElementById("expensesTable");

    // ============================
    // Helper: Handle API Errors
    // ============================

    async function getErrorMessage(response) {
        try {
            const errorData = await response.json();
            return errorData.detail || "خطایی رخ داده است.";
        } catch {
            return "خطایی در ارتباط با سرور رخ داده است.";
        }
    }

    // ============================
    // Create / Update Expense
    // ============================

    if (createExpenseForm) {

        const descriptionInput = document.getElementById("description");
        const amountInput = document.getElementById("amount");
        const submitButton = createExpenseForm.querySelector(".submit-btn");

        let editingId = null;

        // Create cancel button dynamically
        const cancelButton = document.createElement("button");

        cancelButton.type = "button";
        cancelButton.textContent = "لغو ویرایش";
        cancelButton.className = "cancel-btn";
        cancelButton.hidden = true;

        createExpenseForm.appendChild(cancelButton);

        // Reset form to create mode
        function resetForm() {
            editingId = null;

            createExpenseForm.reset();

            submitButton.textContent = "ثبت هزینه";
            cancelButton.hidden = true;
        }

        // Cancel editing
        cancelButton.addEventListener("click", resetForm);

        // Form submission
        createExpenseForm.addEventListener("submit", async (event) => {

            event.preventDefault();

            const description = descriptionInput.value.trim();
            const amount = Number(amountInput.value);

            if (!description || !Number.isFinite(amount) || amount <= 0) {
                alert("لطفاً توضیحات و مبلغ معتبر وارد کنید.");
                return;
            }

            const expenseData = {
                description: description,
                amount: amount
            };

            const isEditing = editingId !== null;

            const url = isEditing
                ? `/costs/${editingId}`
                : "/costs";

            const method = isEditing ? "PUT" : "POST";

            try {

                submitButton.disabled = true;
                submitButton.textContent = "در حال ارسال...";

               const params = new URLSearchParams({
                    description: description,
                    amount: amount
                });

                const response = await fetch(`/costs?${params.toString()}`, {
                    method: "POST"
                });

                if (!response.ok) {
                    throw new Error(await getErrorMessage(response));
                }

                alert(
                    isEditing
                        ? "هزینه با موفقیت ویرایش شد."
                        : "هزینه با موفقیت ثبت شد."
                );

                window.location.reload();

            } catch (error) {

                alert(error.message);

                submitButton.disabled = false;
                submitButton.textContent = isEditing
                    ? "ذخیره تغییرات"
                    : "ثبت هزینه";
            }
        });

        // ============================
        // Edit Expense
        // ============================

        if (expensesTable) {

            expensesTable.addEventListener("click", (event) => {

                const editButton = event.target.closest(".edit-expense");

                if (!editButton) return;

                const row = editButton.closest("tr");

                if (!row) return;

                editingId = editButton.dataset.id;

                descriptionInput.value = row
                    .querySelector(".expense-description")
                    .textContent.trim();

                amountInput.value = row
                    .querySelector(".expense-amount")
                    .dataset.amount;

                submitButton.textContent = "ذخیره تغییرات";
                cancelButton.hidden = false;

                createExpenseForm.scrollIntoView({
                    behavior: "smooth",
                    block: "center"
                });

                descriptionInput.focus();
            });
        }
    }

    // ============================
    // Delete Expense
    // ============================

    if (expensesTable) {

        expensesTable.addEventListener("click", async (event) => {

            const deleteButton = event.target.closest(".delete-expense");

            if (!deleteButton) return;

            const itemId = deleteButton.dataset.id;

            const confirmed = confirm(
                "آیا از حذف این هزینه اطمینان دارید؟"
            );

            if (!confirmed) return;

            try {

                deleteButton.disabled = true;
                deleteButton.textContent = "در حال حذف...";

                const response = await fetch(`/costs/${itemId}`, {
                    method: "DELETE"
                });

                if (!response.ok) {
                    throw new Error(await getErrorMessage(response));
                }

                alert("هزینه با موفقیت حذف شد.");

                window.location.reload();

            } catch (error) {

                alert(error.message);

                deleteButton.disabled = false;
                deleteButton.textContent = "حذف";
            }
        });
    }

    // ============================
    // Search Expenses
    // ============================

    if (searchInput && expensesTable) {

        searchInput.addEventListener("input", () => {

            const searchValue = searchInput.value.trim().toLowerCase();

            const rows = expensesTable.querySelectorAll("tbody tr");

            rows.forEach((row) => {

                const description = row
                    .querySelector(".expense-description");

                if (!description) return;

                const text = description.textContent
                    .trim()
                    .toLowerCase();

                row.style.display = text.includes(searchValue)
                    ? ""
                    : "none";
            });
        });
    }

});
