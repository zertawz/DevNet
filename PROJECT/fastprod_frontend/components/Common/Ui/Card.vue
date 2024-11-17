<template>
  <v-row justify="center">
    <v-col cols="12">
      <v-card :flat="flat" class="rounded-lg">
        <v-card-title :class="headerClass">
          <v-icon :color="iconColor" class="mr-1">mdi-{{ icon }}</v-icon>
          {{ title }}
        </v-card-title>
        <div>
          <slot name="headerActions"></slot>
        </div>
        <v-card-text>
          <slot name="content"></slot>
        </v-card-text>
        <v-card-actions>
          <slot name="footerActions"></slot>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>
<script>
export default {
  props: {
    title: {
      type: String,
      default: null,
    },
    icon: {
      type: String,
      default: null,
    },
    flat: {
      type: Boolean,
      default: true,
    },
    headerClass: {
      type: String,
      default: 'primary white--text mb-2',
    },
    iconColor: {
      type: String,
      default: 'white',
    },
  },
  data() {
    return {}
  },
}
</script>
<style scoped></style>
