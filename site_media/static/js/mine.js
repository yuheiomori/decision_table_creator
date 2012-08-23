/**
 * Created with PyCharm.
 * User: yuhei
 * Date: 12/07/13
 * Time: 22:59
 * To change this template use File | Settings | File Templates.
 */



!function (a) {
    a(function () {
        "use strict", a.support.transition = function () {
            var b = document.body || document.documentElement,
                c = b.style,
                d = c.transition !== undefined || c.WebkitTransition !== undefined || c.MozTransition !== undefined || c.MsTransition !== undefined || c.OTransition !== undefined;
            return d && {
                end: function () {
                    var b = "TransitionEnd";
                    return a.browser.webkit ? b = "webkitTransitionEnd" : a.browser.mozilla ? b = "transitionend" : a.browser.opera && (b = "oTransitionEnd"), b
                }()
            }
        }()
    })
}(window.jQuery);


var HN, HNterest;
HNterest = function () {
    function a() {
        this.url = "http://api.hnterest.com"

        return a.prototype.route = function (a, b) {
            return this.current = this.url + a, b ? this.url + a + "?page=" + b : this.url + a
        }, a.prototype.active = function (a) {
        return this.route("/active", a)
        }, a.prototype.ask = function (a) {
            return this.route("/ask", a)
        }, a.prototype.best = function (a) {
            return this.route("/best", a)
        }, a.prototype.newest = function (a) {
            return this.route("/newest", a)
        }, a.prototype.noobstories = function (a) {
            return this.route("/noobstories", a)
        }, a.prototype.latest = function (a) {
            return this.route("/latest", a)
        }, a.prototype.current = function (a) {
            return a ? this.current + "?page=" + a : this.current
        }, a
    }(), HN = new HNterest;


var HNRouter, __bind = function (a, b) {
        return function () {
            return a.apply(b, arguments)
        }
    },
    __hasProp = Object.prototype.hasOwnProperty,
    __extends = function (a, b) {function d() {
        this.constructor = a
    }
        for (var c in b) __hasProp.call(b, c) && (a[c] = b[c]);
        return d.prototype = b.prototype, a.prototype = new d, a.__super__ = b.prototype, a
    };
HNRouter = function (a) {function b() {
    this.noobHN = __bind(this.noobHN, this), this.newestHN = __bind(this.newestHN, this), this.latestHN = __bind(this.latestHN, this), this.bestHN = __bind(this.bestHN, this), this.askHN = __bind(this.askHN, this), this.activeHN = __bind(this.activeHN, this), b.__super__.constructor.apply(this, arguments)
}
    return __extends(b, a), b.prototype.routes = {
        "/ask": "askHN",
        "/active": "activeHN",
        "/best": "bestHN",
        "/latest": "latestHN",
        "/newest": "newestHN",
        "/noobstories": "noobHN"
    }, b.prototype.activeHN = function () {
        return this.view.fetchFeeds(HN.active(), !0)
    }, b.prototype.askHN = function () {
        return this.view.fetchFeeds(HN.ask(), !0)
    }, b.prototype.bestHN = function () {
        return this.view.fetchFeeds(HN.best(), !0)
    }, b.prototype.latestHN = function () {
        return this.view.fetchFeeds(HN.latest(), !0)
    }, b.prototype.newestHN = function () {
        return this.view.fetchFeeds(HN.newest(), !0)
    }, b.prototype.noobHN = function () {
        return this.view.fetchFeeds(HN.noobstories(), !0)
    }, b
}(Backbone.Router), window.AppRouter = new HNRouter;
var HNCollection, HNModel, HNView, __hasProp = Object.prototype.hasOwnProperty,
    __extends = function (a, b) {function d() {
        this.constructor = a
    }
        for (var c in b) __hasProp.call(b, c) && (a[c] = b[c]);
        return d.prototype = b.prototype, a.prototype = new d, a.__super__ = b.prototype, a
    },
    __bind = function (a, b) {
        return function () {
            return a.apply(b, arguments)
        }
    };
HNModel = function (a) {function b() {
    b.__super__.constructor.apply(this, arguments)
}
    return __extends(b, a), b
}(Backbone.Model), HNCollection = function (a) {function b() {
    b.__super__.constructor.apply(this, arguments)
}
    return __extends(b, a), b.prototype.model = HNModel, b.prototype.url = HN.latest(), b
}(Backbone.Collection), window.AppCollection = new HNCollection, HNView = function (a) {function b() {
    this.render = __bind(this.render, this), this.loadFeeds = __bind(this.loadFeeds, this), this.fetchFeeds = __bind(this.fetchFeeds, this), this.initialize = __bind(this.initialize, this), b.__super__.constructor.apply(this, arguments)
}
    return __extends(b, a), b.prototype.el = ".column", b.prototype.initialize = function () {
        var a;
        return this.page = "", this.router = AppRouter, this.router.view = this, this.collection = AppCollection, Backbone.history.start(), this.collection.bind("reset", this.render), a = Backbone.history.fragment, this.router.routes[a] ? ($(".loader").show(), this.router.navigate("/" + a, {
            trigger: !0
        })) : a !== "" && ($(".loader").show(), this.collection.fetch({
            success: this.clearBar,
            error: this.errorBar
        })), this.arrangeBoxes()
    }, b.prototype.clearBar = function () {
        return $(".loader").hide(), $(".failed-loader").hide()
    }, b.prototype.errorBar = function () {
        return $(".loader").hide(), $(".failed-loader").show()
    }, b.prototype.arrangeBoxes = function () {
        return $(".column .box").wookmark({
            offset: 30
        })
    }, b.prototype.fetchFeeds = function (a, b) {
        return b == null && (b = !1), b && $(this.el).html(""), this.collection.url = a, $(".loader").show(), this.collection.fetch({
            success: this.clearBar,
            error: this.errorBar
        })
    }, b.prototype.loadFeeds = function () {
        var a;
        return this.page !== "" ? a = HN.current + "?page=" + this.page : a = HN.current, this.fetchFeeds(a)
    }, b.prototype.render = function () {
        var a = this;
        return this.collection.each(function (b) {
            var c, d, e, f, g, h;
            c = b.toJSON(), a.page = c.nextId, g = c.items, h = [];
            for (e = 0, f = g.length; e < f; e++) d = g[e], $(a.el).append(ich.hnbox(d)).fadeIn("slow"), h.push(a.arrangeBoxes());
            return h
        })
    }, b
}(Backbone.View), $(window).resize(function () {
    return App.arrangeBoxes()
}), $(window).scroll(function () {
    if (App.page !== "" && $(window).scrollTop() === $(document).height() - $(window).height()) return App.loadFeeds()
}), $(document).ready(function () {
    var a, b;
    return a = !1, b = "", key("r", function () {
        return App.fetchFeeds(HN.current, !0)
    }), key("n", function () {
        if (App.page !== "") return App.loadFeeds()
    }), key("a", function () {
        return a === !1 ? (a = !0, $(".autorefresh").fadeIn("slow"), b = setInterval(function () {
            return App.fetchFeeds(HN.current, !0)
        }, 3e5)) : (a = !1, $(".autorefresh").fadeOut("slow"), clearInterval(b))
    }), $(".showabout").click(function () {
        return $("#about").modal("show")
    }), window.App = new HNView
});
