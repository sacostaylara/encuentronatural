# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons import decimal_precision as dp


class PosOrder(models.Model):
    _inherit = 'pos.order'

    margin = fields.Float('Margin', compute='_compute_margin', store=True, digits=dp.get_precision('Product Price'))

    @api.multi
    @api.depends('lines.margin')
    def _compute_margin(self):
        for order in self:
            order.margin = sum(order.mapped('lines.margin'))


class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    margin = fields.Float('Margin', compute='_compute_multi_margin', store=True, digits=dp.get_precision('Product Price'))
    purchase_price = fields.Float('Cost Price', compute='_compute_multi_margin', store=True, digits=dp.get_precision('Product Price'))

    @api.multi
    @api.depends('product_id', 'qty', 'price_subtotal')
    def _compute_multi_margin(self):
        for line in self:
            if not line.product_id:
                line.purchase_price = 0
                line.margin = 0
            else:
                line.purchase_price = line.product_id.standard_price
                line.margin = line.price_subtotal - line.purchase_price * line.qty


class PosOrderReport(models.Model):
    _inherit = 'report.pos.order'

    margin = fields.Float(string='Margin', readonly=True)

    def _select(self):
        ret = super(PosOrderReport, self)._select()
        return ret.replace('s.date_order AS date,', 's.date_order AS date, SUM(l.margin) as margin,')
