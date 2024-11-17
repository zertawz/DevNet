// import * as VeeValidate from 'vee-validate'
import {
  required,
  confirmed,
  email,
  alpha,
  digits,
  numeric,
  regex,
} from "vee-validate/dist/rules";
import {
  ValidationProvider,
  ValidationObserver,
  extend,
  localize,
} from "vee-validate";
// import attributesFr from 'vee-validate/dist/locale/fr'
import fr from "vee-validate/dist/locale/fr.json";
import Vue from "vue";

Vue.component("ValidationProvider", ValidationProvider);
Vue.component("ValidationObserver", ValidationObserver);

localize("fr", fr);
extend("required", required);
extend("confirmed", confirmed);
extend("alpha", alpha);
extend("digits", digits);
extend("regex", regex);
extend("numeric", numeric);
extend("decimal", {
  validate: (value, { decimals = "*", separator = "." } = {}) => {
    if (value === null || value === undefined || value === "") {
      return {
        valid: false,
      };
    }

    if (Number(decimals) === 0) {
      return {
        valid: /^-?\d*$/.test(value),
      };
    }
    const regexPart = decimals === "*" ? "+" : `{1,${decimals}}`;
    // eslint-disable-next-line no-unused-vars
    const regex = new RegExp(
      `^[-+]?\\d*(\\${separator}\\d${regexPart})?([eE]{1}[-]?\\d+)?$`
    );
    value = Number(value);

    return {
      valid: regex.test(value),
    };
  },
  message:
    "Le champ {_field_} doit contenir seulement un chiffre décimal par exemple: 500 ou 500.50",
});
