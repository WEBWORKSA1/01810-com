/* ============================================================
   01810.com — SITE CONFIGURATION (edit this file only)
   ============================================================ */
window.SITE_CONFIG = {
  siteName: "01810",
  tagline: "Markets & Fortune",
  siteUrl: "https://01810.com",
  interestUrl: "https://web.works/contact",

  /* Owner inbox — stored encoded; assembled at runtime only.
     Never write the plain address anywhere in HTML. */
  _k: 23,
  _m: [122,120,116,57,123,126,118,122,112,87,38,118,100,124,101,120,96,117,114,96],

  /* Google AdSense: paste your publisher ID, e.g. "ca-pub-1234567890123456".
     Leave empty to show "Advertise here" house ads in every slot.
     Also update /ads.txt with the same ID. */
  adsenseClient: "",
  adsenseSlots: { leader: "", rect: "", inart: "", tall: "" },

  /* Analytics (optional): GA4 measurement ID, e.g. "G-XXXXXXX" */
  ga4: "",

  /* Donations: PayPal donate uses the owner inbox (assembled at runtime).
     Optionally add Buy Me a Coffee / Stripe Payment Links / Ko-fi URLs. */
  paypalDonate: true,
  buyMeACoffeeUrl: "",
  stripeLinks: { once: "", monthly: "" },

  /* YouTube: your channel URL + videos shown on the site (IDs are replaceable) */
  youtubeChannel: "https://www.youtube.com/results?search_query=01810+markets+fortune",
  videos: [
    { id: "G2lVtp2Pd_Q", title: "The Hang Seng Index explained in one minute", cat: "markets", by: "Investing Expat" },
    { id: "hXAbIy6RmrM", title: "Hang Seng Indices 101: Everything you need to know", cat: "markets", by: "LifeChamp" },
    { id: "th4ouIJnyT8", title: "What is the Hang Seng 50 Index?", cat: "markets", by: "Capital.com" },
    { id: "emyh5ESXWRs", title: "The evolution of the Hang Seng Index over half a century", cat: "markets", by: "Hang Seng Bank" },
    { id: "sr673iAqLZY", title: "Meanings behind Chinese numbers — which are lucky?", cat: "numbers", by: "Chinese with Christine" },
    { id: "wf13M4MoHS4", title: "Chinese lucky and unlucky numbers explained", cat: "numbers", by: "Learn Chinese Now" },
    { id: "QwvlAbisiRc", title: "Most lucky and unlucky numbers for Chinese people", cat: "numbers", by: "Off the Great Wall" },
    { id: "ZLWRPtmgYw8", title: "How to calculate your Kua number", cat: "fengshui", by: "Julie Khuu" },
    { id: "bJag2BvLnBY", title: "The Great Race — story of the Chinese zodiac", cat: "fengshui", by: "Mythology Unleashed" }
  ],

  /* Social profiles (leave "" to hide) */
  social: { youtube: "https://www.youtube.com/", x: "", instagram: "", tiktok: "", linkedin: "" },

  /* Current contest (dates in ISO format, local midnight) */
  contestEnds: "2026-10-31T23:59:59+08:00"
};
