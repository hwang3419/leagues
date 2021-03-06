var check_load = function (thisbutton, e, eOpts){
    env.teams = teams[thisbutton.originalValue]
    env.league = thisbutton.originalValue
    Ext.getCmp('homeselectfield').setOptions(env.teams)
    Ext.getCmp('awayselectfield').setOptions(env.teams)
    Ext.getCmp('awayselectfield').setValue(env.teams[2].text)
}

var submit_form = function(thisbutton, e, eOpts){
    var form_value = {}
    form_value['HomeTeam'] = Ext.getCmp('homeselectfield').getValue()
    form_value['AwayTeam'] = Ext.getCmp('awayselectfield').getValue()
    if(form_value['HomeTeam'] == form_value['AwayTeam']){
        Ext.Msg.alert('ugh','Home & Away can not be same!!');
        return
    }
    form_value['order_by'] = '-Date'
    query_string = Ext.urlEncode(form_value)
    window.location = '/match/'+env.league+'/?'+query_string
}

var switch_form = function(){
    var h = Ext.getCmp('homeselectfield').getValue()
    var a = Ext.getCmp('awayselectfield').getValue()
    Ext.getCmp('awayselectfield').setValue(h)
    Ext.getCmp('homeselectfield').setValue(a)

}
var radio = {
                xtype: 'panel',
                layout: {
                    type: 'hbox',
                    align: 'middle',
                },
                items: [
                    {
                        xtype: 'radiofield',
                        label: ' ',
                        labelCls: 'england',
                        padding:'0,0,0,0',
                        margin:'0,0,0,0',
                        value:'e0',
                        width:5,
                        labelAlign:'right',//'top',
                        flex: 1,
                        name:'league',
                        checked: true,
                        listeners:{
                            check: check_load
                        }
                    },
                    {
                        xtype: 'radiofield',
                        label: ' ',
                        labelCls: 'italy',
                        labelAlign:'right',//'top',
                        flex: 1,
                        name:'league',
                        value:'i1',
                        listeners:{
                            check: check_load
                        }
                    },
                    {
                        xtype: 'radiofield',
                        label: ' ',
                        labelCls: 'germany',
                        labelAlign:'right',//'top',
                        flex: 1,
                        name:'league',
                        value:'d1',
                        listeners:{
                            check: check_load
                        }
                    },
                    {
                        xtype: 'radiofield',
                        label: ' ',
                        labelCls: 'spain',
                        labelAlign:'right',//'top',
                        flex: 1,
                        name:'league',
                        value:'sp1',
                        listeners:{
                            check: check_load
                        }
                    }
                ],
            
            }
var query_form = [
        radio,
        {
            xtype: 'selectfield',
            label: 'Home',
            id : 'homeselectfield',
            valueField:'text',
            options:teams['e0']
        }, {
        xtype : 'selectfield',
        label : 'Away',
        id : 'awayselectfield',
        valueField:'text',
        value:teams['e0'][2].text,
        options:teams['e0'],
        }, {xtype: 'panel',
            layout: {
                    type: 'hbox',
                    align: 'middle',
                },
            items:[{
            xtype: 'button',
            text: 'Switch Home&Away',
            //centered: true,
            width:100,
            listeners:{
                tap: switch_form,
            }
        },{
            xtype: 'button',
            text: 'GO',
            centered: true,
            width:100,
            listeners:{
                tap: submit_form
            }
        }]
        },
    ]

