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
    ResPartner.fields.push('payment_method_id');

    models.load_models({
        model: 'res.partner.payment.method',
        fields: ['id', 'name', 'code'],
        loaded: function(self, paymentmethods) {
            self.paymentmethods = paymentmethods;
        },
    });

});