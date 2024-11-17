<template>
  <v-app dark>
    <v-navigation-drawer :clipped="true" fixed app >
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          color="primary"
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar :clipped-left="true" fixed app color="primary" class="white--text" flat>
      <v-toolbar-title v-text="title" />
      <v-icon class="white--text">mdi-code-tags</v-icon>
      <v-spacer />
      version 1.0.0
    </v-app-bar>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>

    <v-footer :absolute="!fixed" app>
      <span>By &copy;  Amar KANTAS - {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: "DefaultLayout",
  data() {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
        {
          icon: "mdi-view-dashboard",
          title: "Dashboard",
          to: "/",
        },
        {
          icon: "mdi-server",
          title: "Inventory",
          to: "/inventory",
        },
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: "FastProduction",
    };
  },
};
</script>
