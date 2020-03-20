        var app = angular.module('app', ['loadOnDemand']);
        app.config(['$loadOnDemandProvider', function ($loadOnDemandProvider) {
            var modules = [
                {
                    name: 'whiteboard',     // name of module
                    script: '/albus/dist/whiteboard.min.js' // path to javascript file
                }
            ];
            $loadOnDemandProvider.config(modules);
        }]);
