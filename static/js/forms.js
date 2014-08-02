var check_load = function (thisbutton, e, eOpts){
    env.teams = teams[thisbutton.originalValue]
}

var radio = {
                xtype: 'panel',
                layout: {
                    type: 'hbox',
                    align: 'middle'
                },
                items: [
                    {
                        xtype: 'radiofield',
                        label: 'ENG',
                        labelCls: 'england',
                        value:'e0',
                        labelAlign:'top',
                        flex: 1,
                        name:'league',
                        checked: true,
                        listeners:{
                            check: check_load
                        }
                    },
                    {
                        xtype: 'radiofield',
                        label: 'ITA',
                        labelCls: 'italy',
                        labelAlign:'top',
                        flex: 1,
                        name:'league',
                        value:'i1',
                        listeners:{
                            check: check_load
                        }
                    },
                    {
                        xtype: 'radiofield',
                        label: 'GER',
                        labelCls: 'germany',
                        labelAlign:'top',
                        flex: 1,
                        name:'league',
                        value:'d1',
                        listeners:{
                            check: check_load
                        }
                    },
                    {
                        xtype: 'radiofield',
                        label: 'ESP',
                        labelCls: 'spain',
                        labelAlign:'top',
                        flex: 1,
                        name:'league',
                        value:'sp1',
                        listeners:{
                            check: check_load
                        }
                    }
                ],
            
            }

var team_form = Ext.create('Ext.form.Panel', {
            height:50,
            width:100,
            items: [
                {
                    xtype: 'fieldset',
                    title: 'Select',
                    items: [
                        {
                            xtype: 'selectfield',
                            label: 'Choose one',
                            options: [
                                {text: 'First Option',  value: 'first'},
                                {text: 'Second Option', value: 'second'},
                                {text: 'Third Option',  value: 'third'}
                            ]
                        }
                    ]
                }
            ]
        });

var query_form = [
        radio,
        {
            xtype: 'selectfield',
            name : 'name',
            label: 'Name',
            options: teams['e0'] 
        },
    ]

