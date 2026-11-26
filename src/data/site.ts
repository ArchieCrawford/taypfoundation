export const site = {
  name: "TAYP Foundation Inc.",
  shortName: "TAYP Foundation",
  url: "https://taypfoundation.com",
  email: "support@taypfoundation.org",
  instagram: "https://www.instagram.com/taypfoundation",
  instagramHandle: "@taypfoundation",
  tayp: "https://mytayp.com",
  tagline: "Youth • Sports • Education • Community",
  foundingDate: "2026-11-12",
  foundingLabel: "November 12, 2026",
} as const;

export const nav = [
  { href: "/about/", label: "About" },
  { href: "/programs/", label: "Programs" },
  { href: "/media-showcase-classic/", label: "Showcase" },
  { href: "/sponsors/", label: "Sponsors" },
  { href: "/contact/", label: "Contact" },
] as const;

export const classic = {
  name: "Media Showcase Classic 7v7",
  path: "/media-showcase-classic/",
  date: "2027-05-22",
  dateLabel: "Saturday, May 22, 2027",
  weekday: "Saturday",
  month: "May",
  day: "22",
  year: "2027",
  place: "Bell Memorial Park",
  city: "Milton, GA",
  sponsor: "Chick-fil-A Milton",
  charity: "North Fulton Community Charities",
  charityUrl: "https://nfcchelp.org/",
  summary:
    "Georgia high school athletes and student media share one field. Play the game, learn the craft, and send a percentage of sponsorships back into the community.",
} as const;

export const classicPartners = [
  { name: "Chick-fil-A Milton", role: "Official event sponsor" },
  { name: "Player Guard", role: "Partner" },
  { name: "Media Kingz", role: "Partner" },
  { name: "Patch", role: "Media partner" },
  { name: "Zorts", role: "Team registration" },
] as const;

export const programs = [
  {
    id: "student-media",
    title: "Student media and journalism credentials",
    summary:
      "A credential for student reporters, photographers, and sideline hosts who cover Georgia high school sports.",
    paragraphs: [
      "High school sports deserve to be covered by the students who live them. We are building a credential for student reporters, photographers, and sideline hosts: a short course, a clear code of conduct, and a pass they can show when they arrive to work a game.",
      "Applications are coming soon. We will publish who can apply, what the credential covers, and how a school day on the sideline is supposed to work before we ask anyone to sign up.",
    ],
  },
  {
    id: "camps",
    title: "Camps and clinics",
    summary:
      "Skill camps for athletes and clinics for the students who tell their stories, on the same ground.",
    paragraphs: [
      "We want athletes and student storytellers learning side by side. Clinics for the game itself, and clinics for the craft of covering it: interviewing, shooting, and filing a story on a deadline.",
      "Dates, host sites, and registration are coming soon. When a camp is real, you will find the plan on this page.",
    ],
  },
  {
    id: "gear",
    title: "Gear drives",
    summary:
      "Cleats, cameras, and the everyday gear that decides who gets to play and who gets to document the game.",
    paragraphs: [
      "A season can turn on a pair of cleats that fit, or a camera a student can borrow for Friday night. We will collect gear and say exactly where it goes.",
      "Our first drive is coming soon. If you have equipment to give, or a team that needs it, write us and we will keep you close to the details.",
    ],
  },
  {
    id: "scholarships",
    title: "Scholarships",
    summary:
      "Awards for students who give something back to a team, a classroom, a newsroom, or a neighborhood.",
    paragraphs: [
      "We intend to award scholarships to students who show up for other people. The size of each award will depend on what the Foundation can responsibly fund, and we will say that number out loud before anyone applies.",
      "Scholarships are coming soon. Criteria, dates, and the application will be public before a single student is asked to fill one out.",
    ],
  },
] as const;

export const board = [
  { role: "Chairperson", name: "Name to be announced" },
  { role: "Vice Chair", name: "Name to be announced" },
  { role: "Treasurer", name: "Name to be announced" },
  { role: "Secretary", name: "Name to be announced" },
] as const;

export const tiers = [
  {
    name: "Community",
    detail: "Placeholder tier. Benefits will be published before anyone is asked to commit.",
  },
  {
    name: "Sideline",
    detail: "Placeholder tier. Benefits will be published before anyone is asked to commit.",
  },
  {
    name: "Varsity",
    detail: "Placeholder tier. Benefits will be published before anyone is asked to commit.",
  },
  {
    name: "Championship",
    detail: "Placeholder tier. Benefits will be published before anyone is asked to commit.",
  },
] as const;

export const partnerPlaceholders = ["Partner name", "Partner name", "Partner name", "Partner name"] as const;

export function organizationJsonLd() {
  return {
    "@type": "NonprofitOrganization",
    "@id": `${site.url}/#organization`,
    name: site.name,
    alternateName: site.shortName,
    url: site.url,
    logo: `${site.url}/brand/logo.webp`,
    email: site.email,
    foundingDate: site.foundingDate,
    slogan: "Youth, Sports, Education, Community",
    areaServed: {
      "@type": "AdministrativeArea",
      name: "Georgia",
    },
    sameAs: [site.instagram, site.tayp],
    description:
      "TAYP Foundation Inc. supports Georgia youth through sports, media education, and community.",
  };
}

export function classicEventJsonLd() {
  return {
    "@type": "SportsEvent",
    "@id": `${site.url}${classic.path}#event`,
    name: classic.name,
    description: classic.summary,
    startDate: classic.date,
    eventAttendanceMode: "https://schema.org/OfflineEventAttendanceMode",
    eventStatus: "https://schema.org/EventScheduled",
    url: `${site.url}${classic.path}`,
    image: `${site.url}/og.jpg`,
    location: {
      "@type": "Place",
      name: classic.place,
      address: {
        "@type": "PostalAddress",
        addressLocality: "Milton",
        addressRegion: "GA",
        addressCountry: "US",
      },
    },
    organizer: { "@id": `${site.url}/#organization` },
    sponsor: {
      "@type": "Organization",
      name: classic.sponsor,
    },
  };
}
