const textarea = document.getElementById("texto");

if (textarea) {

    textarea.addEventListener("input", function () {

        const limite = 500;

        if (this.value.length > limite) {

            this.value = this.value.substring(
                0,
                limite
            );

        }

    });

}