<template>
  <div>
    <v-dialog v-model="dialog" :max-width="width">
      <v-card>
        <v-toolbar v-if="!!header" color="primary" dark>
          <v-icon>mdi-{{ header.icon }}</v-icon>
          <h4 class="ml-2">{{ header.label }}</h4>
          <v-spacer></v-spacer>
          <v-btn icon dark @click="dialog = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-toolbar>
        <v-card-text>
          <slot name="content"></slot>
        </v-card-text>
        <v-card-actions class="justify-end">
          <slot name="action"></slot>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  props: {
    width: {
      type: String,
      default: '800',
    },
    header: {
      type: Object,
      default: null,
    },
  },
  data() {
    return {
      dialog: false,
    }
  },
  methods: {
    open() {
      this.dialog = true
    },
    close() {
      this.dialog = false
    },
  },
}
</script>
<style scoped></style>
