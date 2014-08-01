var check_load = function (thisbutton, e, eOpts){
    console.log(thisbutton,thisbutton.originalValue)

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

query_form = [
        radio,
        {
            xtype: 'textfield',
            name : 'name',
            label: 'Name'
        },
    ]
