const SecurePassword = {
    password_length: 6,
    password_counter: 1,
    allowedValuesString: '',
    allowedValues: {
        uppercase: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        lowercase: 'abcdefghijklmnopqrstuvwxyz',
        numbers: '0123456789',
        symbols: '!@#$%^&*()_+'
    },
    validateChecked: function(){
        const chkboxes = document.getElementsByClassName("custom-control-input");
        let numberChecks = 0;
        Array.prototype.forEach.call(chkboxes, function(el) {
            if (el.checked) {
                numberChecks+=1;
            }
        });
        if (numberChecks==0) {
            throw new Error("Debe seleccionar al menos una opción de valores permitidos.");
        }
    },
    generate: function () {
        this.validateChecked();    
        this.password_length = parseInt(document.getElementById("password_length").value);
        this.password_counter = parseInt(document.getElementById("password_count").value);
        const ul = document.getElementById('ul_passwords');
        ul.innerHTML = '';
        this.getAllowedValuesString();
        for (let i = 0; i < this.password_counter; i++) {
            let li = document.createElement('li');
            li.className = "list-group-item d-flex justify-content-between lh-condensed";
            li.textContent = this.getPassword();
            ul.appendChild(li);
        }
        document.getElementById("span_pass_number").textContent = this.password_counter;
    },
    getAllowedValuesString: function () {
        if (document.getElementById("chk_uppercase").checked) {
            this.allowedValuesString += this.allowedValues.uppercase;
        }
        if (document.getElementById("chk_lowercase").checked) {
            this.allowedValuesString += this.allowedValues.lowercase;
        }
        if (document.getElementById("chk_numbers").checked) {
            this.allowedValuesString += this.allowedValues.numbers;
        }
        if (document.getElementById("chk_symbols").checked) {
            this.allowedValuesString += this.allowedValues.symbols;
        }
    },
    getPassword: function () {
        let password = '';
        for (let i = 0; i < this.password_length; i++) {
            let random = Math.floor(Math.random() * this.allowedValuesString.length);
            password += this.allowedValuesString[random];
        }
        return password;
    }
};

(function () {
    'use strict'
    window.addEventListener('load', function () {
        const $frm = document.getElementById("frmSecurePass");
        $frm.addEventListener("submit", (e) => {
            e.preventDefault();
            try {
                const oSecurePassword = Object.create(SecurePassword);
                oSecurePassword.generate();
            } catch (err) {
                alert(err.message);
                console.warn(err.message);
            }
        });
    }, false)
}())