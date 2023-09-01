import { createRouter, createWebHistory } from "vue-router";

import Room from "../views/Room.vue";
import WaitingRoom from "../views/WaitingRoom.vue";
import Game from "../views/Game.vue";
import Watch from "../views/Watch.vue";

const routes = [
  { path: "/", component: Room },
  { path: "/room/:roomId/waiting", component: WaitingRoom },
  { path: "/room/:roomId/game", component: Game },
  { path: "/room/:roomId/watch", component: Watch },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
