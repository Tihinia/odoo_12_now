# -*- coding: utf-8 -*-
# Модель данных для хранения информации о табелях
from odoo import models, fields

class table(models.Model):
    _name = 'table.table'
    date_add_table=fields.Date(string='Дата создания')
    date_up_table=fields.Date(string='Дата корректировки')
    person_name = fields.Char(string='Исполнитель')
    reporting_period_month=fields.Selection([('Январь','январь'),('Февраль','февраль'),('Март','март'),
    ('Апрель','апрель'),('Май','май'),('Июнь','июнь'),('Июль','июль'),('Август','август'),('Сентябрь','сентябрь'),
    ('Октябрь','октябрь'),('Ноябрь','ноябрь'),('Декабрь','декабрь')],string='Месяц отчетного периода')
    reporting_period_year=fields.Selection([('2020','2020'),('2021','2021'),('2022','2022'),
    ('2023','2023')],string='Год отчетного периода')
    description=fields.Text(string='Примечания')
    otdel=fields.Char(string='Отдел/объект')

class indextable(models.Model):
    _name = 'index_table.index_table'
    familiy=fields.Many2one('hr.employee')
    # imiy=fields.Char(string='Имя')
    # otchestvo=fields.Char(string='Отчество')
    doljnost=fields.Char(string='Должность')
    kolvo_otrab_dnei=fields.Integer(string='Количество отработанных дней')
    kolvo_otrab_chas=fields.Float(string='Количество отработанных часов',digits = (1,1))
    tabel_nomer=fields.Integer(string='Табельный номер')
    den_1=fields.Float(string='1',digits = (1,1))
    den_2=fields.Float(string='2',digits = (1,1))
    den_3=fields.Float(string='3',digits = (1,1))
    den_4=fields.Float(string='4',digits = (1,1))
    den_5=fields.Float(string='5',digits = (1,1))
    den_6=fields.Float(string='6',digits = (1,1))
    den_7=fields.Float(string='7',digits = (1,1))
    den_8=fields.Float(string='8',digits = (1,1))
    den_9=fields.Float(string='9',digits = (1,1))
    den_10=fields.Float(string='10',digits = (1,1))
    den_11=fields.Float(string='11',digits = (1,1))
    den_12=fields.Float(string='12',digits = (1,1))
    den_13=fields.Float(string='13',digits = (1,1))
    den_14=fields.Float(string='14',digits = (1,1))
    den_15=fields.Float(string='15',digits = (1,1))
    den_16=fields.Float(string='16',digits = (1,1))
    den_17=fields.Float(string='17',digits = (1,1))
    den_18=fields.Float(string='18',digits = (1,1))
    den_19=fields.Float(string='19',digits = (1,1))
    den_20=fields.Float(string='20',digits = (1,1))
    den_21=fields.Float(string='21',digits = (1,1))
    den_22=fields.Float(string='22',digits = (1,1))
    den_23=fields.Float(string='23',digits = (1,1))
    den_24=fields.Float(string='24',digits = (1,1))
    den_25=fields.Float(string='25',digits = (1,1))
    den_26=fields.Float(string='26',digits = (1,1))
    den_27=fields.Float(string='27',digits = (1,1))
    den_28=fields.Float(string='28',digits = (1,1))
    den_29=fields.Float(string='29',digits = (1,1))
    den_30=fields.Float(string='30',digits = (1,1))
    den_31=fields.Float(string='31',digits = (1,1))