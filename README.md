<!-- Animated Header -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:7E3BF2,100:00D4FF&height=200&section=header&text=Samuel%20Mbabhazi&fontSize=42&fontColor=FFFFFF&animation=fadeIn&fontAlignY=35&desc=Senior%20Full-Stack%20Engineer%20%7C%20Code%20Merged%20Into%20Mongoose%20%26%20The%20NestJS%20Ecosystem&descSize=16&descAlignY=55&descAlign=50" width="100%"/>

  <br/>

  <img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=600&size=22&duration=3000&pause=1000&color=7E3BF2&center=true&vCenter=true&multiline=true&repeat=true&width=800&height=80&lines=TypeScript-First+Architecture+%7C+NestJS+%7C+Angular+%7C+Next.js;My+code+ships+in+libraries+downloaded+millions+of+times+a+week" alt="Typing SVG" />

  <br/>
  <a href="mailto:samuelmbabhazi@gmail.com">
    <img src="https://img.shields.io/badge/Hire%20Me-Email-FF5722?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
  <a href="https://linkedin.com/in/samuelmbabhazi">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://www.upwork.com/freelancers/~013636cfc522b0d380">
    <img src="https://img.shields.io/badge/Hire%20Me-Upwork-14A800?style=for-the-badge&logo=Upwork&logoColor=green" />
  </a>
  <a href="https://samuelmbabhazi.com">
    <img src="https://img.shields.io/badge/Portfolio-samuelmbabhazi.com-7E3BF2?style=for-the-badge&logo=googlechrome&logoColor=white" />
  </a>
  <a href="https://dev.to/samuelmbabhazi">
    <img src="https://img.shields.io/badge/Tech%20Articles-dev.to-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white" />
  </a>

  <br/><br/>

  <img src="https://komarev.com/ghpvc/?username=samuelmbabhazi&color=7E3BF2&style=flat-square&label=Profile+Views"/>

</div>

<br/>

## Open Source Impact

> My pull requests are reviewed and merged by the maintainers of some of the most used libraries in the JavaScript ecosystem.
> Every line below links to a real, verifiable contribution.

<div align="center">

  <a href="https://github.com/Automattic/mongoose/pull/16406">
    <img src="https://img.shields.io/npm/dw/mongoose?style=for-the-badge&logo=mongoose&label=Mongoose%20·%20my%20fix%20ships%20here&color=7E3BF2" />
  </a>
  <a href="https://github.com/nestjs/cache-manager/pull/962">
    <img src="https://img.shields.io/npm/dw/%40nestjs%2Fcache-manager?style=for-the-badge&logo=nestjs&label=NestJS%20cache-manager%20·%20my%20feature%20ships%20here&color=7E3BF2" />
  </a>

</div>

<br/>

| Project | Contribution | Proof |
|---------|--------------|-------|
| [**Mongoose**](https://github.com/Automattic/mongoose) <br/> *The MongoDB ODM for Node.js* | Fixed a type system regression where `Model.schema` resolved to `any` on handwritten model annotations, restoring typed schema access for every project that writes `Model<T>` by hand. **Merged by the maintainer without a single change requested.** | [PR #16406](https://github.com/Automattic/mongoose/pull/16406) · Merged |
| [**nestjs/cache-manager**](https://github.com/nestjs/cache-manager) <br/> *Official NestJS caching module* | Added support for `Cacheable` instances with `nonBlocking` mode in the cache provider factory. **Shipped in [release 3.1.0](https://github.com/nestjs/cache-manager/releases).** | [PR #962](https://github.com/nestjs/cache-manager/pull/962) · Released |
| [**Ever Gauzy**](https://github.com/ever-co/ever-gauzy) <br/> *Open business management platform* | Diagnosed a TypeORM 1.0 migration regression that broke the Employees and Candidates pages in production, reproduced it against the live demo API, and shipped the two line fix with the exact normalization idiom the migration used elsewhere. **Merged in under three hours.** Plus earlier API correctness patches and Angular component improvements. | [PR #9840](https://github.com/ever-co/ever-gauzy/pull/9840) · Merged |
| [**nestjs/mongoose**](https://github.com/nestjs/mongoose) <br/> *Official NestJS Mongoose module* | Authored the root cause analysis for the `Model.schema` typing issue and proposed a `ModelWithSchema<T>` type verified against mongoose 7, 8 and 9, alongside the upstream Mongoose fix above. | [PR #2859](https://github.com/nestjs/mongoose/pull/2859) · In review |
| [**Ever Teams**](https://github.com/ever-co/ever-teams) & [**Ever Traduora**](https://github.com/ever-co/ever-traduora) | Service layer improvements, state management and real time collaboration features; REST API and Angular rendering fixes in the translation workflow. | Merged |

<div align="center" style="margin-top: 15px;">
  <a href="https://github.com/Automattic/mongoose">
    <img src="https://img.shields.io/github/stars/Automattic/mongoose?style=for-the-badge&logo=mongoose&label=Mongoose&color=7E3BF2" />
  </a>
  <a href="https://github.com/nestjs/cache-manager">
    <img src="https://img.shields.io/github/stars/nestjs/cache-manager?style=for-the-badge&logo=nestjs&label=NestJS%20Cache%20Manager&color=7E3BF2" />
  </a>
  <a href="https://github.com/ever-co/ever-gauzy">
    <img src="https://img.shields.io/github/stars/ever-co/ever-gauzy?style=for-the-badge&logo=github&label=Ever%20Gauzy&color=7E3BF2" />
  </a>
  <a href="https://github.com/ever-co/ever-teams">
    <img src="https://img.shields.io/github/stars/ever-co/ever-teams?style=for-the-badge&logo=github&label=Ever%20Teams&color=7E3BF2" />
  </a>
</div>

<br/>

## About Me

```typescript
const samuel: SeniorEngineer = {
    title: "Senior Full-Stack Engineer",
    experience: "5+ years shipping production-grade applications",
    openSource: {
        mongoose: "types(model): keep Model.schema typed (PR #16406, merged by the maintainer)",
        nestjsCore: "feat: Cacheable nonBlocking mode support (PR #962, shipped in v3.1.0)",
        everCo: ["Ever Gauzy", "Ever Teams", "Ever Traduora"]
    },
    whatIDoBest: [
        "TypeScript-first backend architecture (NestJS)",
        "Production-grade Angular, React & Next.js frontends",
        "Root cause analysis: reproduce, isolate, fix, prove with tests",
        "Scalable GraphQL & REST APIs"
    ],
    languages: ["Français", "English", "Swahili"],
    availableFor: ["Remote roles", "Freelance projects", "Open-source collaboration"]
};
```

<br/>

## Tech Stack

<div align="center">

### Core

![TypeScript](https://img.shields.io/badge/TypeScript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
![NestJS](https://img.shields.io/badge/NestJS-%23E0234E.svg?style=for-the-badge&logo=nestjs&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
![Angular](https://img.shields.io/badge/Angular-%23DD0031.svg?style=for-the-badge&logo=angular&logoColor=white)
![React](https://img.shields.io/badge/React-%2361DAFB.svg?style=for-the-badge&logo=react&logoColor=black)
![Next.js](https://img.shields.io/badge/Next.js-%23000000.svg?style=for-the-badge&logo=nextdotjs&logoColor=white)
![GraphQL](https://img.shields.io/badge/GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white)

### Data & State

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Prisma](https://img.shields.io/badge/Prisma-2D3748?style=for-the-badge&logo=prisma&logoColor=white)
![TypeORM](https://img.shields.io/badge/TypeORM-%23FE0803.svg?style=for-the-badge&logo=typeorm&logoColor=white)
![RxJS](https://img.shields.io/badge/RxJS-%23B7178C.svg?style=for-the-badge&logo=reactivex&logoColor=white)
![NgRx](https://img.shields.io/badge/NgRx-%23BA2BD2.svg?style=for-the-badge&logo=ngrx&logoColor=white)
![TanStack Query](https://img.shields.io/badge/TanStack%20Query-%23FF4154.svg?style=for-the-badge&logo=reactquery&logoColor=white)

### Delivery

![Docker](https://img.shields.io/badge/Docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![NGINX](https://img.shields.io/badge/NGINX-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![Vitest](https://img.shields.io/badge/Vitest-%236E9F18.svg?style=for-the-badge&logo=vitest&logoColor=white)
![Jest](https://img.shields.io/badge/Jest-%23C21325.svg?style=for-the-badge&logo=jest&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-%2385EA2D.svg?style=for-the-badge&logo=swagger&logoColor=black)

Also at home with: JavaScript · Python · PHP · Bash · MySQL · Express · Apollo · WebSockets · SASS · Figma · Clean Architecture · SOLID · DDD

</div>

<br/>

## GitHub Stats

<div align="center">

  <img height="180em" src="https://streak-stats.demolab.com?user=samuelmbabhazi&background=0D1117&ring=7E3BF2&fire=00D4FF&currStreakLabel=7E3BF2&border=7E3BF2&stroke=7E3BF2&currStreakNum=FFFFFF&sideNums=FFFFFF&sideLabels=FFFFFF&dates=FFFFFF" />

  <br/>

  <img src="https://github-readme-activity-graph.vercel.app/graph?username=samuelmbabhazi&bg_color=0D1117&color=7E3BF2&line=00D4FF&point=FFFFFF&area=true&area_color=7E3BF2&hide_border=false&custom_title=Contribution%20Activity" />

</div>

<br/>

## GitHub Achievements

<div align="center">

| Achievement | Count | Description |
|:-----------:|:-----:|-------------|
| 🤝 **Pair Extraordinaire** | x3 | Consistent collaborative pull request quality |
| 🦈 **Pull Shark** | x3 | High-volume merged pull requests across codebases |

</div>

<br/>

## Tech Articles

I write about NestJS architecture, TypeScript patterns, GraphQL API design, and full-stack engineering on **[dev.to/samuelmbabhazi](https://dev.to/samuelmbabhazi)**.

<div align="center">
  <a href="https://dev.to/samuelmbabhazi">
    <img src="https://img.shields.io/badge/Read%20All%20Articles-dev.to-7E3BF2?style=for-the-badge&logo=devdotto&logoColor=white"/>
  </a>
</div>

<br/>

## Let's Connect

<div align="center">

**Open to remote opportunities and freelance projects**

I build clean, scalable, production-grade applications with TypeScript-first architecture,
and I fix the kind of bugs other people route around. If you value engineering quality
and open-source culture, let's talk.

<br/>

  <a href="mailto:samuelmbabhazi@gmail.com">
    <img src="https://img.shields.io/badge/samuelmbabhazi%40gmail.com-Email-FF5722?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
  <a href="https://samuelmbabhazi.com">
    <img src="https://img.shields.io/badge/Portfolio-samuelmbabhazi.com-7E3BF2?style=for-the-badge&logo=googlechrome&logoColor=white" />
  </a>
  <a href="https://linkedin.com/in/samuelmbabhazi">
    <img src="https://img.shields.io/badge/LinkedIn-samuelmbabhazi-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://github.com/samuelmbabhazi">
    <img src="https://img.shields.io/github/followers/samuelmbabhazi?label=Follow&style=for-the-badge&logo=github&color=0D1117" />
  </a>

  <br/><br/>

  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:7E3BF2,100:00D4FF&height=120&section=footer&animation=fadeIn" width="100%"/>

</div>
