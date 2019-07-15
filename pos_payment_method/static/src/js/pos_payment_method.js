odoo.define('pos_payment_method.pos_payment_method', function(require) {
    "use strict";
    var core = require('web.core');
    var models = require('point_of_sale.models');

    var QWeb = core.qweb;
    var _t = core._t;

    var ResPartner = _.find(models.PosModel.prototype.models, function(p) {
        if (p.model == 'res.partner') {
            return true;
        }
        return false;
    });
    ResPartner.fields.push('Metodo_pago');
    ResPartner.fields.push('Banco_asociado');
    ResPartner.fields.push('Transferencia_Uso');

    models.load_models([{
        model: 'l10n_mx_edi.payment.method',
        fields: ['id', 'name', 'code'],
        loaded: function(self, paymentmethods) {
            self.paymentmethods = paymentmethods;
        },
    },
    {
        model: 'res.partner.bank',
        fields: ['id', 'acc_number', 'bank_id'],
        loaded: function(self, paymentmethods_2) {
            self.paymentmethods_2 = paymentmethods_2;
        },
    },
    {
        model: 'tranferencia.uso',
        fields: ['id','name','codigo'],
        loaded: function(self, paymentmethods_3) {
            self.paymentmethods_3 = paymentmethods_3;
        },
    },

    ]);


    
});
