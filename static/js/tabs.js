Ext.application({
    name: 'Sencha',

    launch: function() {
        //The whole app UI lives in this tab panel
        Ext.Viewport.add({
            xtype: 'tabpanel',
            fullscreen: true,
            tabBarPosition: 'bottom',

            items: [
                // This is the home page, just some simple html
                {
                    title: 'Home',
                    iconCls: 'home',
                    cls: 'home',
                    xtype: 'container',
                    items : query_form,
                },

                // This is the recent blogs page. It uses a tree store to load its data from blog.json
                {
                    title: 'Comments',
                    iconCls: 'compose',
                    cls: 'star',
                    items:[team_form],
                },

                // This is the contact page, which features a form and a button. The button submits the form
                {
                    title: 'About',
                    iconCls: 'info',
                    cls: 'star',
                }
            ]
        });
    }
});
