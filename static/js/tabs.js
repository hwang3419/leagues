Ext.onReady(function(){
    Ext.application({
    name: 'Sencha',
    requires : [
        'Ext.TitleBar'
    ],

    launch: function() {
        //The whole app UI lives in this tab panel
        Ext.Viewport.add({
            xtype: 'tabpanel',
            fullscreen: true,
            tabBarPosition: 'bottom',

            items: [
                // This is the home page, just some simple html
                {
                    iconCls: 'home',
                    cls: 'home',
                    xtype: 'fieldset',
                    items : query_form,
                },

                // This is the recent blogs page. It uses a tree store to load its data from blog.json
                {
                    title: 'Comments',
                    iconCls: 'compose',
                    cls: 'star',
                    items:[],
                },

                // This is the contact page, which features a form and a button. The button submits the form
                {
                    title: 'About',
                    iconCls: 'info',
                    cls: 'star',
                    html:'<h3>Developing...</h3></br>Contact: hwang.iit@gmail.com'
                }
            ]
        });
    }
});
})

